import express from 'express';

const app = express();
const port = Number(process.env.PORT ?? 3000);

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: 'bluehorizon-concierge-agent' });
});

app.use((_req, res) => {
  res.type('html').send(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Blue Horizon Concierge</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 0; min-height: 100vh; display: grid; place-items: center; background: #eef7fb; color: #123; }
      main { max-width: 720px; padding: 3rem; background: white; border-radius: 24px; box-shadow: 0 20px 60px rgba(0, 50, 90, 0.15); }
      h1 { color: #006a8e; }
    </style>
  </head>
  <body>
    <main>
      <h1>Blue Horizon Concierge — coming soon</h1>
      <p>This greenfield scaffold will be built live during the demo with GitHub Copilot plan mode.</p>
    </main>
  </body>
</html>`);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Blue Horizon Concierge placeholder listening on port ${port}`);
});
