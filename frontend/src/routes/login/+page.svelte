<script lang="ts">
	import { goto } from '$app/navigation';
	import AuthShell from '$lib/components/auth/AuthShell.svelte';
	import AuthToggle from '$lib/components/auth/AuthToggle.svelte';
	import AuthField from '$lib/components/auth/AuthField.svelte';
	import SocialAuth from '$lib/components/auth/SocialAuth.svelte';

	let email = $state('');
	let password = $state('');

	async function handleLogin(event: SubmitEvent) {
		event.preventDefault();
		// TODO: call backend auth, set session, then navigate.
		await goto('/app');
	}
</script>

<svelte:head>
	<title>Minstash — Secure Access</title>
</svelte:head>

<AuthShell>
	<AuthToggle active="login" />

	<div class="p-8 pt-4 md:p-10">
		<form class="space-y-6" onsubmit={handleLogin}>
			<AuthField
				id="email"
				label="Email Address"
				type="email"
				placeholder="architect@vault.io"
				autocomplete="email"
				bind:value={email}
			/>

			<AuthField
				id="password"
				label="Security Key"
				type="password"
				placeholder="••••••••"
				autocomplete="current-password"
				hintLabel="Recovery Access?"
				hintHref="#"
				bind:value={password}
			/>

			<button
				type="submit"
				class="mt-4 w-full rounded-xl border border-white/10 bg-accent py-4 font-bold tracking-wide text-white shadow-xl shadow-accent/20 transition-all duration-200 hover:shadow-accent/40 active:scale-[0.98]"
			>
				Authorize Access
			</button>
		</form>

		<SocialAuth />
	</div>
</AuthShell>
