import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";
import { nextCookies } from "better-auth/next-js";
import { Pool } from "pg";

export const auth = betterAuth({
  database: new Pool({
    connectionString: process.env.DATABASE_URL!,
  }),
  emailAndPassword: {
    enabled: true,
  },
  plugins: [
    nextCookies(),
    jwt({
      jwt: {
        issuer: process.env.BETTER_AUTH_URL || "http://localhost:3000",
        expirationTime: "1h",
        definePayload: ({ user }) => ({
          sub: user.id,
          email: user.email,
          name: user.name,
        }),
      },
    }),
  ],
});
