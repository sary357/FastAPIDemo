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
    phone_number varchar(100) not null,
    question varchar(65535) not null,
    answer varchar(65535) not null, 
    vote varchar(100),
    created_at timestamptz not null default current_timestamp,
    vote_at timestamptz,
    PRIMARY KEY (id)
)  TABLESPACE pg_default;  
CREATE INDEX queries_phone_query_idx ON gogobot_log.public.votes (phone_number, question, answer);
CREATE INDEX queries_created_at_idx ON gogobot_log.public.votes (created_at);

create role readonly;
GRANT usage ON schema public TO readonly;
GRANT SELECT ON ALL TABLES IN schema public TO readonly;
GRANT SELECT ON ALL SEQUENCES IN schema public TO readonly;
create user recsys with password 'CHANGE_ME';
GRANT readonly to recsys;