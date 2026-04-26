<script lang="ts">
	type Props = { active: 'login' | 'register' };
	let { active }: Props = $props();
</script>

<div class="flex justify-center p-6 pb-2">
	<div
		class="flex w-full max-w-[280px] rounded-full border border-white/10 bg-white/5 p-1"
	>
		<a
			href="/login"
			class="flex-1 rounded-full py-2 text-center text-xs tracking-tight transition-all duration-300 {active ===
			'login'
				? 'bg-white/10 font-bold text-white shadow-inner'
				: 'font-semibold text-white/40 hover:text-white/80'}"
		>
			Login
		</a>
		<a
			href="/register"
			class="flex-1 rounded-full py-2 text-center text-xs tracking-tight transition-all duration-300 {active ===
			'register'
				? 'bg-white/10 font-bold text-white shadow-inner'
				: 'font-semibold text-white/40 hover:text-white/80'}"
		>
			Sign Up
		</a>
	</div>
</div>
