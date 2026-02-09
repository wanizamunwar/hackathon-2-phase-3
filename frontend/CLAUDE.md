# Frontend — Next.js

## Tech Stack
- Next.js 16+ (App Router), TypeScript 5+, Tailwind CSS
- Better Auth for authentication (email/password + JWT plugin)
- Client-side API wrapper in `src/lib/api.ts`

## Patterns
- **App Router**: Pages in `src/app/`, layouts, route groups `(auth)`
- **Components**: Reusable UI in `src/components/`
- **Lib**: Shared utilities in `src/lib/` (auth, api client)
- **Middleware**: `src/middleware.ts` protects `/dashboard` routes

## Auth Flow
1. Better Auth handles signup/signin on Next.js server
2. JWT token issued and stored client-side
3. API client attaches JWT to all backend requests
4. Backend verifies JWT independently using shared secret

## Conventions
- Use `"use client"` directive for interactive components
- Server components by default, client components when needed
- Tailwind for all styling — no CSS modules
- Form validation on client side before API calls

## Running
```bash
cd frontend
npm install
npm run dev
```
