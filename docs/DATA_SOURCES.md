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