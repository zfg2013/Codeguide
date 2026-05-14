# 0001 Use MkDocs Material

Date: 2026-05-06  
Status: Accepted  
Owner: Departing lab member

## Context

The lab needs a searchable internal knowledge base before key workflow knowledge leaves with graduating or departing members. Future maintainers may not be software engineers.

## Options Considered

| Option | Pros | Cons |
| --- | --- | --- |
| MkDocs Material | Markdown-first, searchable, simple GitHub Pages deployment | Requires basic Git workflow |
| Wiki-only documentation | Easy browser editing | Harder to test and review as a repository |
| Database-backed web app | Flexible permissions and forms | Too much maintenance for an MVP |

## Decision

Use MkDocs Material with Markdown files in a GitHub repository.

## Consequences

- The MVP has no database and no login system.
- Documentation can be reviewed through pull requests.
- GitHub Pages can host the static site.
- The lab should keep pages simple and avoid custom plugins unless there is a clear maintenance benefit.
