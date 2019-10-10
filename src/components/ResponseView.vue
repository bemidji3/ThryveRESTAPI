<template lang="pug">
    md-card
        md-card-header
            md-card-header-text Response:
        md-card-content
            .over-view
                ResponseCard(v-for="(res, index) in response.over" :res="res" :title="index" :keyword="'over'")
            .under-view
                ResponseCard(v-for="(res, index) in response.under" :res="res" :title="index" :keyword="'under'")
            .equals-view
                ResponseCard(v-for="(res, index) in response['equal']" :res="res" :title="index" :keyword="'equal'")
</template>

<script>
    import ResponseCard from "./ResponseCard";
    export default {
        name: "ResponseView",
        components: {
            ResponseCard
        },
        props : {
            response: {}
        },

        mounted(){
            this.letMeSeeTheResponse();
        },
        methods: {
            letMeSeeTheResponse(){
                console.log("this is the over response inside response view");
                console.log(this.response);

                console.log("these are the Object keys inside the response view: ");
                console.log(Object.keys(this.response.over))


            }
        }
    }
</script>

<style scoped lang="stylus">



</style>