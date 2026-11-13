# Data sources

## Chosen source
Greenhouse public Job Board API (https://docs.greenhouse.io/job-board.html)

## Why
- Public JSON, no key needed (per Greenhouse docs).
- Full job descriptions via content=true.

## Terms check
Greenhouse docs state GET endpoints are public and need no authentication. They state no usage restrictions. Postings belong to the employers, so raw data is not committed to this repo (data/ is gitignored).

## Companies used
<list the board tokens you will use>

## Fields kept
id, title, location, updated_at, absolute_url, content, departments, offices

## Not stored
Any personal contact details.