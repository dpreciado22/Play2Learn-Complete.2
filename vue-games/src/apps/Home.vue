<template>
  <div class="container py-4">
    <h1 class="mb-3">Play2Learn Games</h1>
    <p class="text-muted">Pick a game to start playing:</p>

    <div class="row g-3">
      <div class="col-md-6">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">Math Facts Practice</h5>
            <p class="card-text">Beat the clock on arithmetic drills.</p>
            <router-link class="btn btn-primary" :to="{ name: 'math-facts' }">Play Math Facts</router-link>
          </div>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">Anagram Hunt</h5>
            <p class="card-text">Unscramble letters to make words.</p>
            <router-link class="btn btn-primary" :to="{ name: 'anagram-hunt' }">Play Anagram Hunt</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default { name: 'HomeView' }
</script>
