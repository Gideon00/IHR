CREATE TABLE "physicians" (
    "id" INTEGER,
    "firstName" TEXT NOT NULL,
    "surName" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "hash" TEXT NOT NULL,
    "date_joined" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id")
);

CREATE TABLE "patient" (
    "id" INTEGER,
    "firstName" TEXT NOT NULL,
    "surName" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "date_joined" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id")
);

CREATE TABLE "relations" (
    "physician_id" INTEGER,
    "patient_id" INTEGER,
    FOREIGN KEY("physician_id") REFERENCES "physicians"("id") ON DELETE CASCADE,
    FOREIGN KEY("patient_id") REFERENCES "patient"("id") ON DELETE CASCADE
);

CREATE TABLE "sessions" (
    "physician_id" INTEGER,
    "patient_id" INTEGER,
    "clinical note" TEXT,
    "transcript" TEXT,
    "audio" TEXT,
    FOREIGN KEY("physician_id") REFERENCES "physicians"("id") ON DELETE CASCADE,
    FOREIGN KEY("patient_id") REFERENCES "patient"("id") ON DELETE CASCADE
);