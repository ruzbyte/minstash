<script lang="ts">
	type Props = {
		id: string;
		label: string;
		type?: 'text' | 'email' | 'password';
		placeholder?: string;
		value?: string;
		autocomplete?: string;
		hintLabel?: string;
		hintHref?: string;
	};

	let {
		id,
		label,
		type = 'text',
		placeholder = '',
		value = $bindable(''),
		autocomplete,
		hintLabel,
		hintHref
	}: Props = $props();
</script>

<div class="group space-y-2">
	<div class="ml-1 flex items-end justify-between">
		<label
			for={id}
			class="font-label block text-[10px] tracking-widest uppercase text-primary/70"
		>
			{label}
		</label>
		{#if hintLabel}
			<a
				href={hintHref ?? '#'}
				class="text-[10px] tracking-tight text-primary/80 transition-colors hover:text-white"
			>
				{hintLabel}
			</a>
		{/if}
	</div>
	<div class="relative">
		{#if type === 'email'}
			<input
				{id}
				name={id}
				type="email"
				{placeholder}
				{autocomplete}
				bind:value
				class="font-body w-full rounded-xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-on-surface backdrop-blur-sm transition-all duration-300 placeholder:text-white/20 focus:border-primary/50 focus:ring-1 focus:ring-primary/20 focus:outline-none"
			/>
		{:else if type === 'password'}
			<input
				{id}
				name={id}
				type="password"
				{placeholder}
				{autocomplete}
				bind:value
				class="font-body w-full rounded-xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-on-surface backdrop-blur-sm transition-all duration-300 placeholder:text-white/20 focus:border-primary/50 focus:ring-1 focus:ring-primary/20 focus:outline-none"
			/>
		{:else}
			<input
				{id}
				name={id}
				type="text"
				{placeholder}
				{autocomplete}
				bind:value
				class="font-body w-full rounded-xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-on-surface backdrop-blur-sm transition-all duration-300 placeholder:text-white/20 focus:border-primary/50 focus:ring-1 focus:ring-primary/20 focus:outline-none"
			/>
		{/if}
	</div>
</div>
