<template lang="pug">
    md-card
        md-card-header
            md-card-header-text Response:
        md-card-content
            .over-view
                ResponseCard(v-for="res in response.over" :title="Object.keys(res)[0]" :responseArray="res[Object.keys(res)[0]]")
            .under-view
                ResponseCard(v-for="res in response.under" :title="Object.keys(res)[0]" :responseArray="res[Object.keys(res)[0]]")
            .equals-view
                ResponseCard(v-for="res in response.equal" :title="Object.keys(res)[0]" :responseArray="res[Object.keys(res)[0]]")
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
        }
    }
</script>

<style scoped lang="stylus">

</style>