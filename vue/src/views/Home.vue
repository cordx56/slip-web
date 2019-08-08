<template lang="pug">
  #home
    b-container(fluid).mb-4.text-center
      b-container
        h1 SILang
        h3 Simple Interpreter Language  <small class="text-secondary">beta</small>
        h5.text-secondary v0.1.0-beta, Codename: Atlas
    b-container
      h4 What can I do with SILang?
      h5 Try SILang coding!
      p
        | Implemented functions: 
        a(href="https://github.com/cordx56/silang/wiki/Implementation-Progress", target="_blank") Implementation Progress
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
