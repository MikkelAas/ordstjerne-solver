<script lang="ts">
	import getWords from '../services/fetchWords';

	let isLoading = false;

	let words = [''];

	async function handleSolveClick(): Promise<void> {
		isLoading = true;

		const object = {
			letters: Array.from(letters),
			specialLetter: specialLetter
		};

		getWords(object)
			.then((result) => {
				if (!(result instanceof Error)) {
					words = result.words;
				} else {
					words = ['Unable to find any words.']
				}
			})
			.catch((error) => {
				return;
			})
			.finally(() => {
				isLoading = false;
			});
	}

	let letters: string;
	let specialLetter: string;
</script>

<div class="main">
	<div class="header">
		<h1>Ordstjerne</h1>
	</div>
	<div class="input">
		<input
			maxlength="7"
			minlength="7"
			type="text"
			id="letters"
			bind:value={letters}
			placeholder="Letters"
		/>
		<br />
		<input
			maxlength="1"
			minlength="1"
			type="text"
			id="special-letter"
			bind:value={specialLetter}
			placeholder="Special letter"
		/>
		<br />

		<button on:click={handleSolveClick}>Solve</button>
	</div>
	<div class="result">
		{#if isLoading}
			<p>I'm loading...</p>
		{:else}
			{#each words as word}
				<p>{word}</p>
			{/each}
		{/if}
	</div>
	<div class="footer">
		<p>&#x1f680</p>
	</div>
</div>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
			'Open Sans', 'Helvetica Neue', sans-serif;
	}
	.main {
		display: grid;
		grid-template-rows: 10% 15% 65% 10%;
		height: 100vh;
	}
	.header {
		grid-row: 1/2;
		width: 100%;
		text-align: center;
	}
	.input {
		grid-row: 2/3;
		width: 100%;
		height: 100%;
		text-align: center;
	}
	.result {
		grid-row: 3/4;
		overflow-y: scroll;
		text-align: center;
		width: 70%;
	}
	.footer {
		grid-row: 4/5;
		width: 30%;
		margin: auto;
		border-top: 0.01ch black solid;
		text-align: center;
	}
	input {
		margin: 5px;
		padding: 5px;
	}
	button {
		margin: 5px;
		padding: 5px;
	}
</style>
