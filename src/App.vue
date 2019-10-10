<template lang="pug">
    .master-container
        FilterView(@gotResponse="displayResponse")
        ResponseView(:response="filterResponse" v-if="!isEmpty")
</template>

<script>

import ResponseView from './components/ResponseView'
import FilterView from './components/FilterView'

export default {
  name: 'app',
  components: {
    FilterView,
    ResponseView
  },
    data() {
      return {
          filterResponse: {}
      }
    },

    computed: {

      isEmpty(){
          for(var prop in this.filterResponse) {
              if(this.filterResponse.hasOwnProperty(prop))
                  return false;
          }
          return true;
      }

    },

    methods: {
      displayResponse(val){

          console.log("response value: ")
          console.log(val)
          this.filterResponse = val;
      },


    }
}
</script>
<style lang="stylus">
#app
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px
</style>
