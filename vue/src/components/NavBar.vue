<template lang="pug">
  b-navbar(toggleable="sm", type="dark", variant="dark")
    b-container
      b-navbar-brand(to="/") slip
      b-navbar-toggle(target="nav-collapse")
      b-collapse(is-nav)#nav-collapse
        b-navbar-nav.ml-auto
          b-nav-item(to="/") Home
          b-nav-item(href="https://github.com/cordx56/slip", target="_blank") GitHub
</template>

<script>
export default {
  name: "NavBar"
}
</script>
