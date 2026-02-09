"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { signUp } from "@/lib/auth";

export default function SignUpPage() {
  const router = useRouter();

  const handleSignUp = async (data: { email: string; password: string; name?: string }) => {
    const { error } = await signUp.email({
      email: data.email,
      password: data.password,
      name: data.name || "",
    });

    if (error) {
      throw new Error(error.message || "Failed to sign up");
    }

    router.push("/dashboard");
  };

  return <AuthForm mode="signup" onSubmit={handleSignUp} />;
}
