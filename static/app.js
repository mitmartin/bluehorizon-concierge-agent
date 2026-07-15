const log = document.getElementById("log");
const form = document.getElementById("f");
const input = document.getElementById("m");
const send = document.getElementById("send");
const hint = document.getElementById("hint");

function add(role, text) {
  const wrap = document.createElement("div");
  wrap.className = "msg " + (role === "user" ? "user" : "bot");
  const b = document.createElement("div");
  b.className = "bubble";
  b.textContent = text;
  wrap.appendChild(b);
  log.appendChild(wrap);
  log.scrollTop = log.scrollHeight;
  return b;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  add("user", text);
  input.value = "";
  send.disabled = true;
  hint.textContent = "Horizon Helper is thinking…";
  const bubble = add("bot", "…");
  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    bubble.textContent = data.reply || "Sorry, no reply.";
  } catch {
    bubble.textContent = "Network hiccup — please try again.";
  } finally {
    send.disabled = false;
    hint.textContent = "";
    input.focus();
  }
});
