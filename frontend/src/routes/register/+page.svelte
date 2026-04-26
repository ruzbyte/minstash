<script lang="ts">
	import { goto } from '$app/navigation';
	import AuthShell from '$lib/components/auth/AuthShell.svelte';
	import AuthToggle from '$lib/components/auth/AuthToggle.svelte';
	import AuthField from '$lib/components/auth/AuthField.svelte';
	import SocialAuth from '$lib/components/auth/SocialAuth.svelte';

	let displayName = $state('');
	let email = $state('');
	let password = $state('');

	async function handleRegister(event: SubmitEvent) {
		event.preventDefault();
		// TODO: call backend register, set session, then navigate.
		await goto('/app');
	}
</script>

<svelte:head>
	<title>Minstash — Forge Access</title>
</svelte:head>

<AuthShell>
	<AuthToggle active="register" />

	<div class="p-8 pt-4 md:p-10">
		<form class="space-y-6" onsubmit={handleRegister}>
			<AuthField
				id="displayName"
				label="Architect Handle"
				type="text"
				placeholder="vault_architect"
				autocomplete="username"
				bind:value={displayName}
			/>

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
				autocomplete="new-password"
				hintLabel="Min 12 chars"
				bind:value={password}
			/>

			<button
				type="submit"
				class="mt-4 w-full rounded-xl border border-white/10 bg-accent py-4 font-bold tracking-wide text-white shadow-xl shadow-accent/20 transition-all duration-200 hover:shadow-accent/40 active:scale-[0.98]"
			>
				Forge Access
			</button>
		</form>

		<SocialAuth label="Provision via GitHub" />
	</div>
</AuthShell>
