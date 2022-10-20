create table if not exists profiles
(
    id  serial
        primary key,
    last_name  varchar(50)  not null,
    first_name varchar(50)  not null,
    email      varchar(255) not null
);

alter table profiles
    owner to postgres;