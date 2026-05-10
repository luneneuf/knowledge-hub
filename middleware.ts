export const config = {
  matcher: ["/((?!_vercel/).*)"],
};

export default function middleware(request: Request): Response | undefined {
  const auth = request.headers.get("authorization");

  if (auth?.startsWith("Basic ")) {
    try {
      const decoded = atob(auth.slice(6));
      const [, password] = decoded.split(":");
      if (password === process.env.SITE_PASSWORD) {
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
