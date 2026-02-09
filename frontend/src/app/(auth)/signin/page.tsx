"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { signIn } from "@/lib/auth";

export default function SignInPage() {
  const router = useRouter();

  const handleSignIn = async (data: { email: string; password: string }) => {
    const { error } = await signIn.email({
      email: data.email,
      password: data.password,
    });

    if (error) {
      throw new Error(error.message || "Invalid credentials");
    }

    router.push("/dashboard");
  };

  return <AuthForm mode="signin" onSubmit={handleSignIn} />;
}
