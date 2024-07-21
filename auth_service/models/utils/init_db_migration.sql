CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE public.clients (
    "Id" UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    "ClientId" character varying(128) COLLATE pg_catalog."default" NOT NULL,
    "ClientSecret" character varying(256) COLLATE pg_catalog."default" NOT NULL,
    "IsAdmin" boolean NOT NULL,
    CONSTRAINT "ClientId" UNIQUE ("ClientId")
);