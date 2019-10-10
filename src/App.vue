<template lang="pug">
    .master-container
        FilterView(@gotResponse="displayResponse")
        ResponseView(v-if="!isEmpty" :response="filterResponse")
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

    methods: {
      displayResponse(val){
          this.filterResponse = val;
      },

        isEmpty(){
          for(let key in this.filterResponse){
              if (this.filterResponse.hasOwnProperty(key)) {
                  return false;
              }
          }

            return true;

        }
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
