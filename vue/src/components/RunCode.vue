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
          pre.slipOutput
            code {{ stdout }}
      b-card(title="Parse tree", v-if="parseTree").my-2
        b-card-text
          pre.slipllvmir
            code {{ llvmir }}
      b-card(title="Error", v-if="stderr").my-2
        b-card-text
          pre.slipErr
            code {{ stderr }}
</template>

<script>
export default {
  name: 'RunCode',
  data() {
    return {
      code: `(defun add (arg1 arg2) (+ arg1 arg2))
(print "Hello, world!")
(print (add 32 24))`,
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
          this.llvmir = response.data.llvmir
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
