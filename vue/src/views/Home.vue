<template lang="pug">
  #home
    b-container(fluid).mb-4.text-center
      b-container
        h1 slip
        h3 Small LIsP Language  <small class="text-secondary">beta</small>
        h5.text-secondary v0.1.0-beta
    b-container
      h4 What can I do with slip?
      h5 Try slip coding!
      p
        | Implemented functions: 
        a(href="https://github.com/cordx56/slip/wiki/Implementation-progress", target="_blank") Implementation Progress
      RunCode
</template>

<script>
import RunCode from '@/components/RunCode.vue'

export default {
  name: 'home',
  components: {
    RunCode
  }
}
</script>
