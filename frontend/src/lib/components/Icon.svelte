<script lang="ts">
	type Props = {
		name: string;
		class?: string;
		filled?: boolean;
	};

	let { name, class: klass = '', filled = false }: Props = $props();

	const style = $derived(
		filled
			? "font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;"
			: "font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;"
	);
</script>

<span aria-hidden="true" class="material-symbols-outlined select-none {klass}" {style}>
	{name}
</span>
