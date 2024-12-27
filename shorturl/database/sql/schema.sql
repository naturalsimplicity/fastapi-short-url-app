-- name: create-table-urls#
create table urls
(
    id integer primary key autoincrement,
    short_id varchar(255) not null unique,
    full_url text not null
);

