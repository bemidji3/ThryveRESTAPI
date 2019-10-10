<template lang="pug">
    md-card
        md-card-header
            md-card-header-text {{ dynamicTitle }}
        md-card-content
            p {{ responseString }}

</template>

<script>
    export default {
        name: "ResponseCard",
        props: {
            title: String,
            keyword: String,
            res: []
        },

        mounted(){
            this.showRes();
        },


        methods: {
            showRes(){
            }
        },


        computed: {

            dynamicTitle () {
                let newTitle = this.title.split(' ');

                if(newTitle[0] === 'Total'){
                    newTitle[0] = 'Fat'
                    console.log("first is Total")
                }

                return newTitle[0] + ' ' + this.keyword + ' ' + newTitle[newTitle.length-1];
            },

            responseString () {


                let returnString = ''
                for(let i = 0; i < this.res.length; i++){
                    let myResponse = this.res[i];

                    returnString += myResponse + '\n';
                }

                return returnString;
            }
        }
    }
</script>

<style scoped lang="stylus">

</style>