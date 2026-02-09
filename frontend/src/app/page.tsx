import { redirect } from "next/navigation";
import { headers } from "next/headers";
import { auth } from "@/lib/auth-server";

export const dynamic = "force-dynamic";

export default async function Home() {
  let hasSession = false;

  try {
    const session = await auth.api.getSession({
      headers: await headers(),
    });
    hasSession = !!session;
  } catch {
    // Auth not ready or no session
  }

  redirect(hasSession ? "/dashboard" : "/signin");
}
