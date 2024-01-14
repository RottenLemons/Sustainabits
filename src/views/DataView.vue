<template>
    <div class="flex flex-column justify-content-center" style="width: 100%; height:92vh; background-color: #588157; opacity: 0.8; background-image: radial-gradient(circle at right 0, #344e41, #588157), repeating-radial-gradient(circle at right 0, #344e41, #344e41, 40px, transparent 80px, transparent 40px); background-blend-mode: multiply;">
        <div class="flex flex-column justify-content-center align-items-center" style="margin-top: 3em;">
            <p style="font-size: 4em; font-weight: bold; color: white; margin-top:0;">
            Data
            </p>

            <DataTable showGridlines :value="users" v-model:filters="filters" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" style="width: 85%">
                <template #header>
                    <div class="flex justify-content-end">
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                        </span>
                    </div>
                </template>
                <Column field="name" header="Name" sortable style="width: 25%"></Column>
                <Column field="country" header="Country" sortable style="width: 25%"></Column>
                <Column field="email" header="Email" sortable style="width: 25%"></Column>
                <Column field="postalZip" header="Zip Code" sortable style="width: 25%"></Column>
            </DataTable>
        </div>
    </div>
</template>



<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Users } from '@/service/Users';
import { FilterMatchMode } from 'primevue/api';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';

onMounted(() => {
    Users.getUsers().then((data) => (users.value = data));
});

const users = ref();
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    'country.name': { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    representative: { value: null, matchMode: FilterMatchMode.IN },
    status: { value: null, matchMode: FilterMatchMode.EQUALS },
    verified: { value: null, matchMode: FilterMatchMode.EQUALS }
});

</script>

