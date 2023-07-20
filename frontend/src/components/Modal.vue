<template>
    <div class="outer-modal">

        <div class="modal" >
            <header class="modal-header">
                <slot name="header">
                </slot>
                
                <button type="button" class="close-btn" @click="close">x</button>
            </header>
            
            <hr>

            <section class="modal-body">
                <slot name="body">
                </slot>
            </section>
            
            <br>

            <footer class="modal-footer">
                <slot name="footer">
                </slot>
                <button type="button" class="-btn" @click="close">close</button>
            </footer>
        </div>
    </div>
</template>

<script lang="ts">
export default{
    name: 'FilterModal',
    methods: {
        close() {
            this.$emit('close');
        }
    }
};
</script>

<style scoped>
@import "../assets/base.css";

.outer-modal{
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal{
    background: var(--vt-c-black-soft);
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    padding: 5%;
    max-width: 80%;
    max-height: 80%;
}

.modal-header{
    display: flex;
    justify-content: space-between;
}

.modal hr{
    margin-top: 10px;    
}

.modal br{
    margin-bottom: 10px;
}

.modal-body{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.modal-footer{
    margin-top: 10px;
}
</style>