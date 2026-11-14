# Data sources

## Chosen source
Greenhouse public Job Board API (https://docs.greenhouse.io/job-board.html)

## Why
- Public JSON, no key needed (per Greenhouse docs).
- Full job descriptions via content=true.

## Terms check
Greenhouse docs state GET endpoints are public and need no authentication. They state no usage restrictions. Postings belong to the employers, so raw data is not committed to this repo (data/ is gitignored).

## Companies used
databricks (more board tokens to be added in P1-03)

## Fields kept
id, title, location, updated_at, absolute_url, content, departments

## Derived later (not collected)
Skills, extracted from content (P1-07).

## Not stored
Personal contact details.

## Data quality findings (Databricks board, 896 jobs, checked 2026-11-14)
- application_deadline is empty in 896 of 896 postings, so it is dropped.
- The language field reports "en" for every posting, including a Japanese-titled one, so it is not reliable. Language filtering will use location and text detection instead.
- content is HTML-escaped (it contains &lt;p&gt; instead of <p>). Cleaning needs html.unescape first, then tag stripping, to get plain text.