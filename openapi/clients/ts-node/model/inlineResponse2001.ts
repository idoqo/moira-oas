/**
 * Moira Alert
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';
import { Contact } from './contact';

export class InlineResponse2001 {
    /**
    * List of all the retrieved Moira contacts.
    */
    'list'?: Array<Contact>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "list",
            "baseName": "list",
            "type": "Array<Contact>"
        }    ];

    static getAttributeTypeMap() {
        return InlineResponse2001.attributeTypeMap;
    }
}

