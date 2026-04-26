
async function createSnippet(title: string, content: string) {
    const response = await fetch(`$/snippets/create`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, content }),
    });

    if (!response.ok) {
        throw new Error("Failed to create snippet");
    }

    return response.json();
}

async function getSnippets() {
    const response = await fetch(`$/snippets`);

    if (!response.ok) {
        throw new Error("Failed to fetch snippets");
    }

    return response.json();
}

export { createSnippet, getSnippets };