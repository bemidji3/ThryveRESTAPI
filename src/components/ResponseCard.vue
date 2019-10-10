<template lang="pug">
    md-card
        md-card-header
            md-card-header-text {{ String }}
        md-card-content
            p {{ responseString }}

</template>

<script>
    export default {
        name: "ResponseCard",
        props: {
            responseArray: [],
            title: String
        },


        computed: {
            responseString () {
                let returnString = ''
                for(let i = 0; i < this.responseArray.length; i++){
                    let myResponse = this.responseArray[i];

                    returnString += myResponse + '\n';
                }

                return returnString;
            }
        }
    }
</script>

<style scoped lang="stylus">

</style>