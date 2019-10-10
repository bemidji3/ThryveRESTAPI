

<template lang="pug">
    .container
        md-card
            md-card-header
                md-card-header-text Select Filters:
            md-card-content
                FilterCard(v-for="filter in filters" @confirm="addToFilters")
            md-card-actions
                md-button(@click="addNewFilter").md-primary.md-raised Add Filter
                md-button(@click="sendRequest").md-accent.md-raised Submit


</template>



<script>


    import FilterCard from './FilterCard.vue'
    export default {
        name: "FilterView",
        data () {
            return {
                filters: [],
                masterFilterObject: {}
            }
        },
        components: {
            FilterCard
        },

        mounted() {
            this.createMasterFilterObject();
        },

        methods: {

            async sendRequest(){
                const myUrl = "http://127.0.0.1:5000/food/return";

                console.log("this is my master filter object");
                console.log(this.masterFilterObject);

                const options = {
                    method: "POST",
                    headers : {
                        'Content-Type' : 'application/json'
                    },
                    body: JSON.stringify(this.masterFilterObject)

                };

                const myRequest = await fetch(myUrl, options);
                const myResponse = await myRequest.json();
                console.log(myResponse);

                this.$emit('gotResponse', myResponse);

            },
            createMasterFilterObject() {
                this.masterFilterObject.over = {};
                this.masterFilterObject.equal = {};
                this.masterFilterObject.under = {};
            },

            addNewFilter(){
                this.filters.push("1");
            },

            addToFilters(val){

                console.log("value: ");
                console.log(val);

                console.log("value[1]" );
                console.log(val[1]);

                console.log('Object.keys(val)[1]');
                console.log(Object.keys(val)[1]);

                console.log('val[Object.keys(val)[1]]');
                console.log(val[Object.keys(val)[1]]);



                //this.filters.push(val);

                switch (val[0]) {
                    case "equal":
                        this.masterFilterObject.equal = {...this.masterFilterObject.equal, ... val[Object.keys(val)[1]]};
                        break;
                    case "under":
                        this.masterFilterObject.under = {...this.masterFilterObject.equal, ... val[Object.keys(val)[1]]};
                        break;
                    case "over":
                        this.masterFilterObject.over = {...this.masterFilterObject.equal, ... val[Object.keys(val)[1]]};
                        break;
                }


                console.log("Master filter object: ");
                console.log(this.masterFilterObject);
            }
        }
    }
</script>

<style scoped lang="stylus">


</style>