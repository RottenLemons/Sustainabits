<script setup lang="ts">
  import Image from 'primevue/image';
  import Button from 'primevue/button';
  import { ref, watch, toRaw } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies';
  import { co2, co2Change, CO2Response } from "@/service/TalkToDB";
  import Calendar from 'primevue/calendar';
  import ProgressBar from 'primevue/progressbar';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import InputNumber from 'primevue/inputnumber';
  import { FilterMatchMode } from 'primevue/api';
  import InputText from 'primevue/inputtext';

  const cookies = useCookies()
  const user = ref(cookies.get('user'));
  cookies.addChangeListener((event) => {
    user.value = event.value;
  })

  const date = ref();
  const editingRows = ref([]);
  const items = ref([{}]);
  const usage = ref(0);
  const limit = ref(0);
  const editable = ref(false);
  const lst: any[] = []

  if (typeof user !== 'undefined' ){    
    watch(date, async (newDate) => {
      let selectedDate = new Date(newDate.getTime() - newDate.getTimezoneOffset() * 60000);
      let response: CO2Response = await co2(user.value.userID, selectedDate.toISOString().split('T')[0])
      items.value = response.items;
      usage.value = response.used;
      editable.value = response.editable;

      if (response.limit != 0) {
        limit.value = response.limit;
      } else {
        limit.value = user.value.co2Limit;
      }
    });

    date.value = new Date();
  }

  const onRowEditSave = (event : any) => {
    lst.push(event);
    let { newData, index } = event;
    if (newData.dol < 0) {
      newData.dol = 0;
    }
    items.value[index] = newData;
  };

  const save = async () => {
    await Promise.all(lst.map(async (element) => {

      let d = toRaw(element['newData'])
      if (d.dol <= 0) {
        await co2Change(user.value.userID, date.value.toISOString().split('T')[0], d['c.categoryID'], d.dol, true)
      } else {
        await co2Change(user.value.userID, date.value.toISOString().split('T')[0], d['c.categoryID'], d.dol, false)
      }
    }));

    let response: CO2Response = await co2(user.value.userID, date.value.toISOString().split('T')[0])
    console.log(response)
    items.value = response.items;
    usage.value = response.used;
  };

  const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS }});
</script>

<template>
  <main style="width: 100%;">
    <div v-if="!user" class="flex align-items-center justify-content-center" style="backgroundColor: #344e41; width: 100%; height: 550px;">
      <div class="flex  flex-column align-items-center justify-content-center">
        <p style="font-size: 5em; font-weight: bold; color: white; margin: 0;" class="font">
          Sustainabits
        </p>
        <p style="font-size: 2em; color: white; margin-top: 1em;" class="font">
          Save the planet 1 bit at a time
        </p>
        <RouterLink style="text-decoration: none;" to="/signup">
          <Button style="font-weight: bold; padding: 2rem; font-size: 2.5em; color: white">SIGN UP</Button>
        </RouterLink> 

      </div>
      <img alt="logo" src="../assets/logo.svg" width="400" height="400" />
    </div>

    <div v-if="!user" class="flex flex-column align-items-center justify-content-center" style="backgroundColor: #588157; width: 100%; height: 700px;">
      <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 2em; margin-top: 0em;" class="font">
          Gamify being eco-friendly
      </p>
      <div class="flex align-items-center justify-content-space-around gap-5">
        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%;">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/footprint-6855149-5625022.png" width="200" style="margin-top: -2em; margin-bottom: 2em;"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 0;" class="font text-pretty text-center">
          Track your carbon footprint
          </p>
        </div>

        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/badge-3671711-3061912.png" width="200"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 1em;" class="font text-pretty text-center">
          Earn rewards by complete your goals!
          </p>
        </div>

        <div class="flex flex-column align-items-center justify-content-space-around" style="width: 33%">
          <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/team-battle-7045028-5740242.png" width="200" style="margin-top: -2em; margin-bottom: 2em;"/> 
          <p style="font-size: 2em; font-weight: 300; color: white; margin-bottom: 0; margin-top: 0;" class="font text-pretty text-center">
          Compete with your friends!
          </p>
        </div>
      </div>
    </div>
    
    <div v-if="!user" class="flex align-items-center justify-content-center gap-5" style="backgroundColor: #337357; width: 100%; height: 600px;">
      <Image src="https://cdn3d.iconscout.com/3d/premium/thumb/trees-7404343-6043595.png" width="400"/> 
      <div class="flex flex-column align-items-center">
        <p style="font-size: 4em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">
          What are you waiting for?
        </p>
        <RouterLink style="text-decoration: none;" to="/signup">
          <Button style="font-weight: bold; padding: 2rem; font-size: 2.5em; color: white">SIGN UP</Button>
        </RouterLink> 
      </div> 
    </div>

    <p  v-if="user" style="font-size: 3em; font-weight: bold; color: white; margin-bottom: 0em; margin-top: 0em; backgroundColor: #337357; width: 100%; text-align: center; padding-top: 2rem; padding-bottom: 0rem;" class="font">
          Add how much you spent today to get your emissions!
        </p>

    <div v-if="user" class="flex align-items-center" style="backgroundColor: #337357; width: 100%; min-height: 94vh;">
      <Calendar v-model="date" inline showWeek style="margin-left: 5rem; margin-right: 3rem"/>
      <div class="flex-column align-items-center justify-content-center">
        
        <p style="font-size: 2em; font-weight: bold; color: white; margin-bottom: 0.75em; margin-top: 0.5em;" class="font">
          CO2 Usage: {{ usage.toFixed(2) }} / {{ limit }}
        </p>
        <ProgressBar :value="usage*100/limit" style="width: 50rem; margin-bottom: 2rem; height: 3rem"></ProgressBar>        
        <DataTable  v-model:filters="filters" :globalFilterFields="['category']" v-if="editable" showGridlines paginator :rows="5" v-model:editingRows="editingRows" :value="items" editMode="row" dataKey="id" @row-edit-save="onRowEditSave"
            :pt="{
                table: { style: 'min-width: 50rem' },
                column: {
                    bodycell: ({ state } : any) => ({
                        style:  state['d_editing']&&'padding-top: 0.6rem; padding-bottom: 0.6rem'
                    })
                }
            }"
        >    
          <template #header>
              <div class="flex justify-content-end">
                  <IconField iconPosition="left">
                      <InputIcon>
                          <i class="pi pi-search" />
                      </InputIcon>
                      <InputText style="margin-left: 1rem;" v-model="filters['global'].value" placeholder="Keyword Search" />
                  </IconField>
              </div>
          </template>
                  
            <Column field="category" header="Category" style="width: 70%">
            </Column>
            <Column field="dol" header="Dollar" bodyStyle="text-align:center" style="width: 10%">
                <template #editor="{ data, field }">
                    <InputNumber v-model="data[field]" style="width: 100%;"/>
                </template>
            </Column>
            <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
        </DataTable>

        <DataTable v-if="!editable" showGridlines paginator :rows="5" :value="items" editMode="row" dataKey="id"
            :pt="{
                table: { style: 'min-width: 50rem' }
            }"
        >
            <Column field="category" header="Category" style="width: 70%">
            </Column>
            <Column field="dol" header="Dollar" bodyStyle="text-align:center" style="width: 10%">
            </Column>
        </DataTable>

        <Button v-if="editable"style="font-weight: bold; width: 100%; color: white; margin-top: 1rem; margin-bottom: 2rem;" class="justify-content-center" @click="save">Save</Button>
      </div>
    </div>
  </main>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&display=swap');
  .font {
    font-family: 'Josefin Sans', sans-serif;
  }

  .p-paginator {
    border-radius: 0px;
  }
</style>