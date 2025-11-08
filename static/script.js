document.getElementById("speak-btn").addEventListener("click", async () => {
  const text = document.getElementById("text-input").value.trim();
  if (!text) return alert("Please enter some text!");

  const formData = new FormData();
  formData.append("text", text);

  const res = await fetch("/speak", { method: "POST", body: formData });
  const data = await res.json();

  if (data.error) return alert(data.error);

  const audio = document.getElementById("audio-player");
  audio.src = data.path + "?t=" + new Date().getTime();
  audio.play();
});

document.getElementById("clear-btn").addEventListener("click", () => {
  document.getElementById("text-input").value = "";
  const audio = document.getElementById("audio-player");
  audio.pause();
  audio.src = "";
});
