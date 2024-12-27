-- name: create-new-url$
insert into urls (short_id, full_url)
values (:short_id, :full_url)
returning id;

-- name: get-full-url$
select full_url
from urls
where short_id = :short_id;

-- name: get-short-id$
select short_id
from urls
where full_url = :full_url;
