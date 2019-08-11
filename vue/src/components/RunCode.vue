<template lang="pug">
  #runCode
    b-form(@submit="runCode")#runCodeForm.text-center
      b-form-group(label="Code: ")
        b-form-textarea(v-model="code", required, rows="8")
      p
        b-button(type="submit", variant="outline-primary") Run
    #runCodeResult
      b-card(title="Output", v-if="stdout").my-2
        b-card-text
          pre.silOutput
            code {{ stdout }}
      b-card(title="Parse tree", v-if="parseTree").my-2
        b-card-text
          pre.silParseTree
            code {{ parseTree }}
      b-card(title="Error", v-if="stderr").my-2
        b-card-text
          pre.silErr
            code {{ stderr }}
</template>

<script>
export default {
  name: 'RunCode',
  data() {
    return {
      code: `((x y z) :: double) = (1.2 2.3 3.4)
println "x = " x ", y = " y ", z = " z
{
    x :: string
    x = "Hello,"
    x = x + " world!"
    println x
    y = y + z
}
println "x = " x ", y = " y ", z = " z`,
      stdout: "",
      parseTree: "",
      stderr: ""
    }
  },
  methods: {
    runCode(evt) {
      evt.preventDefault()
      this.stdout = ""
      this.parseTree = ""
      this.stderr = ""
      this.$axios.post("/api/run", { code: this.code }).then((response) => {
        if (response.data.status) {
          this.stdout = response.data.stdout
          this.parseTree = response.data.parseTree
        } else {
          this.stderr = response.data.stderr
        }
      }).catch((error) => {
        this.stderr = String(error)
      })
    }
  }
}
</script>
