export const config = {
  matcher: ["/((?!_vercel/).*)"],
};

export default function middleware(request: Request): Response | undefined {
  const expected = process.env.SITE_PASSWORD;

  if (!expected) {
    return new Response("Server misconfigured: SITE_PASSWORD env var not set", {
      status: 500,
      headers: { "Content-Type": "text/plain; charset=utf-8" },
    });
  }

  const auth = request.headers.get("authorization");

  if (auth?.startsWith("Basic ")) {
    try {
      const decoded = atob(auth.slice(6));
      const [, password] = decoded.split(":");
      if (password === expected) {
        return;
      }
    } catch {
      // 잘못된 base64 — 401로 폴백
    }
  }

  return new Response("Authentication required", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Knowledge Hub"',
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
