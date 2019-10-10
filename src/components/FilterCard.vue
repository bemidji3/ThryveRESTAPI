<template lang="pug">
    md-card
        md-card-content.md-layout
            .dropdown-menu.md-size-30.md-layout-item
                md-field.md-layout-item
                    md-select(v-model="nutrientChoice")
                        md-option(value="203") Protein
                        md-option(value="204") Fat
                        md-option(value="205") Carbohydrate
                        md-option(value="269") Sugar
            .buttons.md-size-30.md-layout-item
                md-radio(v-model="buttonVal" value="over") Above
                md-radio(v-model="buttonVal" value="equal") Equals
                md-radio(v-model="buttonVal" value="under") Below
            .input-field.md-size-30.md-layout-item
                md-field
                    label Amount (g)
                    md-input(v-model="amount" type="number")
            .confirm-button.md-size-10.md-layout-item
                md-button(:style="{'background-color' : backgroundColor}" @click="generateAndConfirm").md-icon-button.md-raised
                    md-icon check



</template>

<script>
    export default {
        name: "FilterCard",
        data() {
            return{
                nutrientChoice: Number,
                amount: Number,
                buttonVal: '',
                confirmed: false,
                backgroundColor: 'red'
            }
        },

        methods: {
            generateAndConfirm (){
                this.confirmed = true;
                this.backgroundColor = 'green';
                this.$emit('confirm', this.filterArray);
            }
        },


        computed: {
             filterArray: function () {
                 let returnArray = [];
                 let returnObject = {};
                 returnObject[this.nutrientChoice] = this.amount;
                 returnArray.push(this.buttonVal);
                 returnArray.push(returnObject);
                 return returnArray
             }
        }
    }
</script>

<style scoped lang="stylus">

    .green-button
        background-color green

    .red-button
        background-color red


</style>