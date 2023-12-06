CREATE DATABASE gogobot_log WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default;

-- Path: sql/create_tables.sql
-- the following table must BE in pg_default tablespace and database "gogobot_log"
create table gogobot_log.public.votes (
    id SERIAL,
    phone varchar(100) not null,
    query varchar(65535) not null,
    response varchar(65535), 
    vote varchar(100),
    created_at timestamptz not null default current_timestamp,
    vote_at timestamptz,
    PRIMARY KEY (id)
)  TABLESPACE pg_default;  
CREATE INDEX queries_phone_query_idx ON gogobot_log.public.votes (phone, query);
CREATE INDEX queries_phone_query_created_idx ON gogobot_log.public.votes (phone, query, created_at);
CREATE INDEX queries_created_at_idx ON gogobot_log.public.votes (created_at);

