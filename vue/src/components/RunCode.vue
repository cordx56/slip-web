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
      b-card(title="LLVM IR", v-if="llvmir").my-2
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
      code: `(defun gcd (a b)
  (if (equal b 0)
    a
    (gcd b (mod a b))))
(print "Hello, world!")
(print (gcd 256 56))`,
      stdout: "",
      llvmir: "",
      stderr: ""
    }
  },
  methods: {
    runCode(evt) {
      evt.preventDefault()
      this.stdout = ""
      this.llvmir = ""
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
