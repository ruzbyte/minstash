import { goto } from "$app/navigation";


class UserState {
    id = $state(0);
    username = $state("");
    isLoggedIn = $state(false);
    cookie = $state<string | null>(null);

    constructor(
        id: number,
        username: string,
        isLoggedIn: boolean,
        cookie: string | null
    ) {
        this.id = id;
        this.username = username;
        this.isLoggedIn = isLoggedIn;
        this.cookie = cookie;
    }

    login(username: string, password: string): Promise<void> {
        return fetch(`/api/login`, {
            method: "POST",
            body: JSON.stringify({ username, password }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.status === "success") {
                    this.isLoggedIn = true;
                    this.username = data.user.username;
                    this.id = data.user.id;
                    this.cookie = document.cookie;
                    goto("/app");
                } else {
                    throw new Error(data.message || "Login failed");
                }
            });
    }

    register(
        username: string,
        password: string,
        retypepassword: string
    ): Promise<void> {
        return fetch(`/api/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password, retypepassword }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.status === "success") {
                    this.isLoggedIn = true;
                    this.username = data.user.username;
                    this.id = data.user.id;
                    this.cookie = document.cookie;
                    goto("/app");
                } else {
                    throw new Error(data.message || "Registration failed");
                }
            });
    }

    logout(): void {
        fetch(`/api/logout`, {
            method: "POST",
        }).catch((error) => {
            console.error("Logout failed:", error);
        }).then(() => {
            document.cookie = "";
            this.isLoggedIn = false;
            this.username = "";
            this.id = 0;
            goto("/");
        });
    }
}

export const user = new UserState(0, "", false, null);