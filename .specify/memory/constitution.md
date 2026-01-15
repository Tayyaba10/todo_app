<!-- SYNC IMPACT REPORT:
Version change: N/A → 1.0.0
Added sections: Core principles based on project requirements
Removed sections: Template placeholders
Templates requiring updates: N/A (new constitution)
Follow-up TODOs: None
-->
# Phase-II Todo Full-Stack Web Application Constitution

## Core Principles

### Spec-Driven Development
Every feature must trace back to a written spec requirement; No manual coding without prior specification; Implementation strictly follows documented plans and tasks.

### Security-First Architecture
JWT-based authentication enforced on every protected route; User data isolation mandatory; Cross-user data access strictly forbidden; All API requests must verify JWT signature.

### Clear Separation of Concerns
Distinct Auth, Backend, and Frontend layers; Backend provides documented APIs consumed by frontend only; Authentication handled separately from business logic.

### Deterministic and Reproducible Outputs
All development artifacts must be reproducible from specs; Build processes must be consistent across environments; Output validation required for all changes.

### Stack Consistency
Fixed technology stack: Next.js 16+ (App Router), FastAPI (Python), SQLModel ORM, Neon Serverless PostgreSQL, Better Auth; No stack deviations without explicit approval; Environment variables clearly specified and consistent.

### Authentication Enforcement
JWT secret shared via BETTER_AUTH_SECRET; User ID derived from JWT, not client input; Unauthorized requests return HTTP 401; Forbidden access returns HTTP 403.

## Additional Constraints

All API routes must require authentication after auth integration; Multi-user task isolation must work correctly; Authenticated users only see their own tasks; Frontend, backend, and auth integrate without manual glue code.

## Development Workflow

Specs → plans → tasks → implementation flow must be reviewable; Every feature must have explicit acceptance criteria; Code changes must be small and testable; All changes reference code precisely.

## Governance

This constitution supersedes all other practices; Amendments require documentation, approval, and migration plan; All PRs/reviews must verify compliance; Code quality, testing, performance, security, and architecture principles must align with these requirements.

**Version**: 1.0.0 | **Ratified**: 2026-01-08 | **Last Amended**: 2026-01-08