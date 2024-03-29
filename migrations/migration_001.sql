CREATE TABLE IF NOT EXISTS "PERSON" (
	"PES_ID"	INTEGER NOT NULL,
	"PES_IMG"	TEXT NOT NULL,
	"PES_NAME"	TEXT NOT NULL,
	"PES_UUID"	TEXT DEFAULT NULL UNIQUE,
	"PES_CARD"	TEXT DEFAULT NULL UNIQUE,
	"PES_TYPE"	TEXT NOT NULL,
	"PES_START_PERIOD"	TIMESTAMP DEFAULT NULL,
	"PES_END_PERIOD"	NUMERIC DEFAULT NULL,
	"PES_DATE_CREATE"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"PES_DATE_UPDATE"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"PES_STATUS"	TEXT NOT NULL DEFAULT 'A',
	PRIMARY KEY("PES_ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "CONFIG" (
	"CFG_KEY"	TEXT NOT NULL,
	"CFG_VALUE"	TEXT NOT NULL,
	"CFG_DATE_CREATE"	TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"CFG_DATE_UPDATE"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("CFG_KEY")
);

CREATE TABLE IF NOT EXISTS "ACCESS" (
	"ACE_ID"	INTEGER NOT NULL,
	"ACE_PES_NAME"	TEXT NOT NULL,
	"ACE_DATE_TIME"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"ACE_ACCURACY"	INTEGER NOT NULL,
	PRIMARY KEY("ACE_ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "ACCESS_CAPTURE" (
	"ACP_ID"	INTEGER NOT NULL,
	"ACP_ACE_ID"	INTEGER NOT NULL,
	"ACP_IMG_REGISTERED"	TEXT NOT NULL,
	"ACP_IMG_CAPTURED"	TEXT NOT NULL,
	"ACP_DATE_CREATE"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("ACP_ACE_ID") REFERENCES "ACCESS"("ACE_ID") ON DELETE CASCADE,
	PRIMARY KEY("ACP_ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "LOG" (
	"LOG_ID"	INTEGER NOT NULL,
	"LOG_DESCRIPTION"	TEXT NOT NULL,
	"LOG_MESSAGE"	TEXT DEFAULT NULL,
	"LOG_STATUS"	TEXT NOT NULL,
	"LOG_DATE_CREATE"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("LOG_ID" AUTOINCREMENT)
);