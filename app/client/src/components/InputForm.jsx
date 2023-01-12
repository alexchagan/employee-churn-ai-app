import React from 'react'
import Select from 'react-select'
import { useController, useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { string, number, z } from 'zod' // validation library
import "./inputForm.css"

const yesNoOptions = [
    { value: "1", label: "Yes"},
    { value: "0", label: "No"},
];

const salaryOptions = [
    { value: "2", label: "High"},
    { value: "1", label: "Medium"},
    { value: "0", label: "Low"},
];

const schema = z.object({
    satisfaction_level: number().gte(0).lte(100).int(),
    last_evaluation: number().gte(0).lte(100).int(),
    number_project: number().int(),
    average_monthly_hours: number().int(),
    time_spend_company: number().int(),
    work_accident: string(),
    promotion_last_5year: string(),
    salary: string(),
});

const InputForm = ({onSave, user={}}) => {
  
  const {register, control, handleSubmit, formState} = useForm({defaultValues: user, resolver: zodResolver(schema)});

  const { field: work_accident_field } = useController({name: 'work_accident', control })
  const { field: promotion_last_5year_field } = useController({name: 'promotion_last_5year', control })
  const { field: salary_field } = useController({name: 'salary', control })
  
  
  const {errors} = formState

  const handleSelectChangeWorkAccident = (option) => {
    work_accident_field.onChange(option.value)
  };

  const handleSelectChangePromotion = (option) => {
    promotion_last_5year_field.onChange(option.value)
  };

  const handleSelectSalary = (option) => {
    salary_field.onChange(option.value)
  };


  const handleSave = (formValues) => {
    onSave(formValues)
  };

  return (
    <form className='Form' onSubmit={handleSubmit(handleSave)}>
        
            <p>What was the employee's satisfaction level from 0 to 100 ?</p>
            <input {...register('satisfaction_level', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.satisfaction_level?.message}</div>
            <p>What was the last evalutioan by the model ?</p>
            <input {...register('last_evaluation', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.last_evaluation?.message}</div>
            <p>How many projects has the employee worked on ?</p>
            <input {...register('number_project', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.number_project?.message}</div>
            <p>How many monthly work hours did the emloyee have ?</p>
            <input {...register('average_monthly_hours', { valueAsNumber: true } )} />
            <div style={{color: "red"}}>{errors.average_monthly_hours?.message}</div>
            <p>How much time did the employee spend in the company in years ?</p>
            <input {...register('time_spend_company', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.time_spend_company?.message}</div>
            <p>Has there ever been a work accident ?</p>
            <div>
                <Select
                value={yesNoOptions.find(({ value }) => value === work_accident_field.label)}
                onChange={handleSelectChangeWorkAccident}
                options={yesNoOptions}
                />
            </div>
            <p>Has the employee gotten a promotion in the last 5 years ?</p>
            <div>
                <Select
                value={yesNoOptions.find(({ value }) => value === promotion_last_5year_field.label)}
                onChange={ handleSelectChangePromotion}
                options={yesNoOptions}
                />
            </div>
            <p>What was the level of salary of the employee ?</p>
            <div>
                <Select
                value={salaryOptions.find(({ value }) => value === salary_field.label)}
                onChange={ handleSelectSalary}
                options={salaryOptions}
                />
            </div>
            
            <button type="submit">Submit</button>
    </form>
  )
}

export default InputForm

