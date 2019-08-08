<template lang="pug">
  b-navbar(toggleable="sm", type="dark", variant="dark")
    b-container
      b-navbar-brand(to="/") SILang
      b-navbar-toggle(target="nav-collapse")
      b-collapse(is-nav)#nav-collapse
        b-navbar-nav.ml-auto
          b-nav-item(to="/") Home
          b-nav-item(to="/about") About
          b-nav-item(href="https://github.com/cordx56/silang", target="_blank") GitHub
</template>

<script>
export default {
  name: "NavBar"
}
</script>
