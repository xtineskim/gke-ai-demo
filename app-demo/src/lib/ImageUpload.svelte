<script>
  let input;
  let container;
  let image;
  let placeholder;
	let showImage = false;

  function onChange() {
    const file = input.files[0];
		
    if (file) {
			showImage = true;

      const reader = new FileReader();
      reader.addEventListener("load", function () {
        image.setAttribute("src", reader.result);
      });
      reader.readAsDataURL(file);
			
			return;
    } 
		showImage = false; 
  }


</script>


<input
	bind:this={input}
	on:change={onChange}
  type="file"
/>
<div bind:this={container}>
	{#if showImage}
		<img bind:this={image} src="" alt="Preview" />
	{:else}
		<span bind:this={placeholder}>Image Preview</span>
	{/if}
</div>
<!-- <button on:click={increment}>
  count is {count}
</button> -->
